import os
import shutil
import re
from pathlib import Path


def collect_files_and_structure(source_dir):
    """第一步：收集所有文件和它们的目录结构"""
    print("\n=== 第一步：收集文件信息 ===")
    file_info = []

    for package_dir in os.listdir(source_dir):
        package_path = os.path.join(source_dir, package_dir)
        if not os.path.isdir(package_path):
            continue

        print(f"\n分析包: {package_dir}")

        # 遍历包下的所有构件目录（倒数第二层）
        for artifact_dir in os.listdir(package_path):
            artifact_path = os.path.join(package_path, artifact_dir)
            if not os.path.isdir(artifact_path):
                continue

            print(f"处理构件: {artifact_dir}")

            # 遍历版本目录
            for version_dir in os.listdir(artifact_path):
                version_path = os.path.join(artifact_path, version_dir)
                if not os.path.isdir(version_path):
                    continue

                # 收集这个版本下所有散列值目录中的文件
                for root, _, files in os.walk(version_path):
                    for file in files:
                        if file.endswith(('.jar', '.pom', '.aar', '.module', '.xml')):
                            file_info.append({
                                'package': package_dir,
                                'artifact': artifact_dir,
                                'version': version_dir,
                                'file': os.path.join(root, file),
                                'filename': file
                            })

    return file_info


def reorganize_structure(source_dir, target_dir, file_info):
    """第二步：重组目录结构并移动文件"""
    print("\n=== 第二步：重组目录结构 ===")
    processed_files = 0

    for info in file_info:
        # 分割包名
        package_parts = info['package'].split('.')

        # 构建目标路径
        target_path = target_dir
        for part in package_parts:
            target_path = os.path.join(target_path, part)

        # 添加构件目录和版本号
        target_path = os.path.join(target_path, info['artifact'], info['version'])

        # 创建目录
        os.makedirs(target_path, exist_ok=True)

        # 复制文件
        target_file = os.path.join(target_path, info['filename'])
        if not os.path.exists(target_file):
            try:
                shutil.copy2(info['file'], target_file)
                processed_files += 1
                print(f"复制文件: {info['filename']} -> {os.path.relpath(target_file, target_dir)}")
            except Exception as e:
                print(f"复制文件失败 {info['filename']}: {str(e)}")

    return processed_files


def main():
    try:
        source_path = input("请输入Maven缓存源目录路径（例如：/xx/files-2.1）: ").strip()
        target_path = input("请输入目标目录路径: ").strip()

        if not os.path.exists(source_path):
            print(f"错误：源目录 {source_path} 不存在！")
            return

        # 第一步：收集文件信息
        file_info = collect_files_and_structure(source_path)
        print(f"\n找到 {len(file_info)} 个文件需要处理")

        # 第二步：重组目录并移动文件
        processed_files = reorganize_structure(source_path, target_path, file_info)

        print(f"\n=== 处理完成 ===")
        print(f"成功处理了 {processed_files} 个文件")

        if processed_files == 0:
            print("\n警告：没有处理任何文件，请检查源目录结构！")

    except Exception as e:
        print(f"\n发生错误：{str(e)}")
        import traceback
        print(traceback.format_exc())


if __name__ == "__main__":
    main()
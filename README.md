# Gradle Cache Reorganizer

A Python tool for reorganizing and optimizing Gradle/Maven cache directory structure. This tool helps you transform the complex hash-based cache directory into a more readable and manageable structure.

## Features

- Automatically collects and analyzes existing cache directory structure
- Supports .jar, .pom, .aar, .module, and .xml files
- Reorganizes directory structure based on package name, artifact, and version
- Maintains file integrity using copy2 to preserve file metadata
- Detailed processing logs
- Error handling and exception reporting

## Requirements

- Python 3.6 or higher
- Operating System: Windows, MacOS, or Linux

## Installation

1. Clone the repository:
```bash
git clone https://github.com/leejay001/gradle-cache-reorganizer.git
cd gradle-cache-reorganizer
```

2. Ensure Python 3.6+ is installed on your system

## Usage

1. Run the script:
```bash
python re_gradle_cache.py
```

2. Follow the prompts to input:
   - Source Maven/Gradle cache directory path
   - Target directory path where you want the reorganized files

3. Wait for the process to complete. The script will show progress and final statistics

### Example

```bash
Please enter Maven cache source directory path (e.g., /xx/files-2.1): /path/to/source/cache
Please enter target directory path: /path/to/target/directory
```

## Directory Structure Example

Before reorganization:
```
files-2.1/
└── com.xx.zz
    └── yysdk
        └── 3.9.0
            ├── 729978d4e2fc23dc587d411e417605c8
            │   └── yysdk-3.9.0.aar
            ├── b45692d8f2fc23dc587d411e987605a2
            │   └── yysdk-3.9.0.pom
            └── a67892d4e2fc23dc587d411e417605f5
                └── yysdk-3.9.0.module
```

After reorganization:
```
target/
└── com
    └── xx
        └── zz
            └── yysdk
                └── 3.9.0
                    ├── yysdk-3.9.0.aar
                    ├── yysdk-3.9.0.pom
                    └── yysdk-3.9.0.module
```

## How It Works

1. The tool scans the source directory (files-2.1) and identifies package directories
2. For each package directory, it processes all artifacts and their versions
3. For each version:
   - It searches through all hash directories to find relevant files (.jar, .pom, .aar, etc.)
   - Each file typically resides in its own hash directory
4. It reorganizes the files by:
   - Breaking down the package name into a proper directory structure (e.g., com.xx.zz → com/xx/zz)
   - Maintaining the artifact name and version
   - Placing all files directly in the version directory without hash folders
5. The result is a clean, intuitive directory structure that's easier to navigate

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

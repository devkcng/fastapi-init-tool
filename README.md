# FastAPI Project Initialization Script

This script initializes a FastAPI project with a predefined structure and configuration files. It sets up the necessary directories, files, and configurations to get you started quickly with a FastAPI application.

## 🛠️ How to Use the Script

Save the file as `fastapi_init.py`.

Run the script to generate your FastAPI project:

### ⚙️ Prerequisites

Before running the script, ensure the following:

- **Python Version**: Python 3.10 or higher is installed on your system.

### 🚀 Running the Script

Clone this repository to your local machine:

```bash
git clone https://github.com/devkcng/fastapi-init-tool.git
```

To initialize your FastAPI project, execute the following command:

```bash
python fastapi-init-tool/fastapi_init.py --init
```

> **Note**  
>
> - Use `python3` instead of `python` if you are on a system where Python 3 is not the default version.  
> - You can specify a custom project name using the `--name` argument. For example:  
>
>   ```bash
>   python fastapi_init.py --init --name my_fastapi_app
>   ```

The script will create a directory with the specified name and set up the following structure:

```
my_fastapi_app/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   ├── services/
│   └── utils/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 🤝 Contributing and Feedback

Feel free to modify this code to suit your project requirements. Contributions, suggestions, and feedback are always welcome!

If you find this script helpful, please consider giving this repository a ⭐ on GitHub. Your support is greatly appreciated!

## 👤 Author

**devkcng**  
GitHub: [https://github.com/devkcng](https://github.com/devkcng)

# Cool Customized CLI
## List of commands:
- start
- convert
- resize
- weather
- quote

## Installation
Clone the repository:
```{bash}
git clone https://github.com/harryypham/custom-cli.git
```

Add the directory to path:
```{bash}
echo 'export PATH="$PATH:$(pwd)/custom"' >> ~/.zshrc
source ~/.zshrc
```

Install supporting modules:
```{bash}
cd custom && pip install -r requirements.txt
```

Set permission:
```{bash}
chmod +x custom/*
```
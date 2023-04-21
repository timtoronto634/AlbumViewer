# AlbumViewer

## installation 


### nodejs
after [installing asdf from here](https://github.com/asdf-vm/asdf)

```
asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git
asdf install
```

## setup
***We are using devcontainer for development.
See [official materials](https://code.visualstudio.com/docs/devcontainers/containers#_forwarding-or-publishing-a-port) for details about devcontainer.***

1. open folder in vscode with .devcontainer extension installed
2. inside dev container,
```
make serve
```
3. access `localhost:8888`
4. you should see raw response of `{"Hello":"World"}`

## Frontend
```
cd frontend
npm install
npm run start
```
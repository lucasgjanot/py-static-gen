from py_static_gen.textnode import TextType, TextNode
import shutil
import os

def copy_delete_content(src, dest):
    shutil.rmtree(dest)

    for item in os.listdir(src):
        caminho_origem = os.path.join(src, item)
        caminho_destino = os.path.join(dest, item)

        if os.path.isdir(caminho_origem):
            shutil.copytree(caminho_origem, caminho_destino, dirs_exist_ok=True)
        else:
            shutil.copy2(caminho_origem, caminho_destino)





def main():
    copy_delete_content("./static", "./public")


if __name__ == "__main__":
    main()

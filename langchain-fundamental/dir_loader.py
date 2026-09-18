from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    DirectoryLoader
)

dir_loader=DirectoryLoader("./data/",glob="**/*.txt")
dir_document=dir_loader.load()

print(dir_document)
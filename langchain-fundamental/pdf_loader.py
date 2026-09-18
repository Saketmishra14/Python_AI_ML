from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    DirectoryLoader
)

pdf_loader=PyPDFLoader("./doc/linux-manual.pdf")
pdf_document=pdf_loader.load()

print(pdf_document)
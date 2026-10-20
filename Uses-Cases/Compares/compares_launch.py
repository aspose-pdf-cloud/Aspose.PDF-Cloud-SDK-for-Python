from compare_pdf_documents import ComparePdfDocuments, Config
from compares_helper import CompareMain

if __name__ == "__main__":
    comparator = CompareMain(Config.CREDENTIALS_FILE)
    pdf_compares = ComparePdfDocuments(comparator.pdf_api, comparator)
    pdf_compares.compareDocument()

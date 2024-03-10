import PyPDF2
from typing import AnyStr
from pydantic import BaseModel, Field
from gentopia.tools.basetool import *

class PdfSearchArgs(BaseModel):
    path: str = Field(..., description="path")

class PdfSearch(BaseTool):
    """Tool that adds the capability to read a PDF file."""
    name = "pdfread"
    description = "A tool that reads and returns the content of a PDF file"
    args_schema:  Optional[Type[BaseModel]] = PdfSearchArgs

    def _run(self, path: AnyStr) -> str:
        res = []

        with open(path, 'rb') as pdfFileObj:
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            for page_num in range(len(pdfReader.pages)):
                page = pdfReader.pages[page_num]
                res.append(page.extract_text())

        return '\n\n'.join(res)

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    ans = PdfSearch()._run("Attention for transformer")
    print(ans)

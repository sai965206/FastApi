'''
pydantic is data validation and format valiation
while work SQL Scheme it's required data format
'''


from pydantic import BaseModel, Field, ConfigDict


class postBase(BaseModel):
	title: str = Field(min_length=1, max_length=50)
	content: str = Field(min_length=1)
	author: str = Field(min_length=1, max_length=50)
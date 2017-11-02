## LIST OF THIRD-PARTY LIBRARIES USED
For installation of below libraries use command from terminal:

`$ pip install <pkg_name>`

* nltk: http://www.nltk.org 
* numpy: http://www.numpy.org/ 
* pandas: http://pandas.pydata.org  
* beautifulsoup4: https://www.crummy.com/software/BeautifulSoup 
* matplotlib: https://matplotlib.org 
* lxml: http://lxml.de 

You can also make use of the requirements.txt file in the root of the source code:

`$ pip install -U -r requirements.txt`

## DATASETS 
* Link to download posts for analysis: https://github.com/aditi137/CZ4045/blob/master/1-DataCollection/OutputData/posts.csv
* Link to download selected posts for annotation: https://github.com/aditi137/CZ4045/blob/master/2-DatasetAnalysisAndAnnotation/3-TokenDefinitionAndAnnotation/OutputData/selectedPosts.csv
* Link to download selected posts manually annotated: https://github.com/aditi137/CZ4045/tree/master/2-DatasetAnalysisAndAnnotation/3-TokenDefinitionAndAnnotation/OutputData/ManuallyAnnotatedPosts

## APPLICATION GUIDE 
1- Project Setup:

* This application runs with the Python 2.7.x interpreter. Add the path of your local python.exe installation to your system PATH variable. Please ensure you have the correct Python version and all dependent libraries (listed above) installed. For every task, the needed data for the scripts are stored in corresponding InputData folder and output results are stored in OutputData folder.
* Please download all of the above datasets before proceeding to the execution step. Detailed download instruction:
Go to https://data.stackexchange.com/stackoverflow/query/new
Use query 1 in Queries file under 1-DataCollection folder to find the data for question posts only. Download result csv file, rename to questions.csv and put under 1-DataCollection/InputData
Run 1-DataCollection/create_queries.py to create a query for answer posts
Copy the query from terminal to query for answer posts. Download result csv, rename to answers.csv and put under 1-DataCollection/InputData 
* Execute below command from terminal to run individual .py files: `$ python <dir_name/file_name>`

In details, the following files should be run:

* Task 1: Collect and process data: 1-DataCollection/process_data.py
* Task 2.1: Stemming: 2-DataAnalysisAndAnnotation/1-Stemming/stemming.py
* Task 2.2: POSTagging: 2-DataAnalysisAndAnnotation/2-POSTagging/pos-tagging.py
* Task 2.3.: Annotate posts: first run 2-DataAnalysisAndAnnotation/3-TokenDefinitionAndAnnotation/postSelector.py to generate a csv file contain 100 posts to be annotated, then run annotation.py (same folder) to create the first version of annotation. Then manual work is done to create final annotation
* Task 3: Tokenize: run 3-Tokenizer/tokenizer.py
* Task 4.1: Irregular token: run 4-FurtherAnalysis/1-IrregularTokens/irregularTokens.py
* Task 4.2: Customized POSTagging: run 4-FurtherAnalysis/1-IrregularTokens/pos_tagging.py
* Task 5: Negation Detection: run 5-NegationExpressionDetection/negationDetection.py

2- Explanations of sample output obtained from your system: 
Explanations are included in the report.

The complete repository with the dataset used and the output data can be found under https://github.com/aditi137/CZ4045

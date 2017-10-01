# CZ4045
## Natural Language Processing - To Do List

### <b>Dataset Collection (10 marks)</b> 
- Dataset needs to contain 500 threads of discussion
- All threads need to pertain to one particular Programming Language
- Each selected thread should have at least two posts. A post can be either a question or an answer.

<b>For the report:</b>
- Document how the dataset was collected and justify it satisﬁes the three conditions 
- Show the statistics of the dataset:
- Number of questions
- Number of answers
- Distribution of the answers (e.g percentage of questions having one, two, or more answers) 
- Length of the posts in number of words (using an off-the-shelf tokenizer).
          

### <b> Dataset Analysis and Annotation (30 marks) </b>
- Stemming of the dataset using an off-the-shelf toolkit
- Identify the top-20 most frequent words(excluding stop words) before and after performing stemming.
- List the original words of the top-20 most frequent stems

- POS Tagging of 10 randomly selected from the dataset 
- Deﬁne tokens in the context of Stack Overﬂow discussion. 

- Randomly select at least 100 posts, and then annotate the sentences based on your token deﬁnition. 
The annotated dataset will be used as ground truth in the next section. You may use http://brat.nlplab.org/ for your annotation task.

<b>For the report:</b>
- Show and discuss results


### <b>Tokenizer (30 marks)</b> 
- Tokenize all sentences in your dataset
- Either use regular expression or CRF(do not create your own, use a library)
- If regular expressions are not used, use a cross validation to evaluate the effectiveness of the tokenzier used (K-fold cross validation is mentioned in the assignment document)
- If you use regular expressions, you can evaluate the results based on the 100 annotated posts. 

<b>For the report:</b>
- If CRF is used, report the Precision, Recall, and F1 of your model
- Analysis of the errors (e.g., case studies on false positives and false negatives).


### <b>Further Analysis (20 marks)</b>
Irregular Tokens:
- Tokenize the dataset using your own tokenizer. 
- Identify the top-20 most frequent tokens which are NOT standard English words (including their morphological forms). 
POS Tagging: 
- Randomly select 10 sentences from the dataset where each sentence contains at least one irregular token. 
- Apply POS tagging on the sentences based on your own tokenization results. 

<b>For the report:</b>
- Show and discuss the tagging results.


### <b>Application (10 marks)</b>
- Deﬁne and develop a simple NLP application based on the dataset. 
- E.g detecting sentences containing Negation Expression using regular expressions. 
(Negation is often expressed through negative words such as no, not, never, none, nobody) 
- You may deﬁne your own application with similar (estimated) difﬁculty level.







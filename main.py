
from transformers import pipeline
cls = pipeline("sentimemnt-analysis")
cls("i hate eating baban")


from transformes import pipeline

clf = pipeline("zero-shot-classification")

clf( "this course all about transformers library",
         candidate_labels=["education","polictics","business"]
   )
--------------------------------------

from transformers import pipeline 

generator = pipeline("text-generation", model="distilgpt2")
generator(
               " in this course, we will teach you how to", 
                 max_length=30,
                 num_return_sequences=2,
   )

--------------------------------------
 
from transformers import pipeline 

cls = pipeline( "fill-mask")
cls("this course will teach you all about <mask> models", top_k=2)
 
------------------------------------------------
##  name recognition ####

from transformers import pipeline 

ner = pipeline("ner", grouped_entities=True)
ner( "my name is noor saed from Pakistan working as ai developer")

--------------------------------------------

from transformers import pipeline 

ner = pipeline("ner", grouped_entities=True)
ner("my name is saed, want to work ")

---------------------------------------------

from transformers import pipeline

question_answer = pipeline("question-answering")

question_answer( question="",
                                context="" )

-------------------------

from transformers import pipeline

summarizer = pipeline("summarization")

summarizer("""
                              """")

-------------------------------------------

from transformers import pipeline

translator = pipeline( "translation", model= "helsinki-NLP/opus-mt-fr-en")

translator("ce cours est produit par huggingface projects")

--------------------------------------------
index.html

<body   style ="backgournd: black ; color:white">

<div class="container mt-4">
            <h1>nlp text: pipeline</h1>
</div>

<form method="post">
         <div class="form-group">
                  <label for="user_input">Enter Text: </label>
                  <textarea class= "form_control" id="user_input" name="user_input" rows="4" required></textarea>
</div>

<div class="form-group">
     <label for="task">choose a task:</label>
     <select class="form-control" id="task" name="task">
            <option value="sentiment">sentiment analysis</select>
             <option value="generation">text generztion</option>
       </select>

</div>
<button type="submit" class="btn btn-primary">submit</button>
</form>

{% if sent %}
<div  class="mt-4">
      <h2> sentiment analysis</h2>
      <p>{{sent[0].label}} , score : {{sent[0].score}}</p>
</div>
{% endif %}

</div>

</body>


-------------------------------------backend ---------
from flask import flask, 

from transformers import pipelone 

#make piepeline 

app= flask(__name__)

#load nlp pipeline 
sentiment_pipeline= pipeline("sentiment-analysis")
generaiton_pipeline = pipeline("generation)

@app.route('/',methods=['post",'get"])

def index():
     sent = none
     gen =none 

      if  request.method=="post":
               user_input= request.form.get('user_input')
                task = request.form.get("task")

                 if task== 'sentiment':
                         sent = sentiment_pipeline(user_input)
                          return  render_template('pipeline.html',sent=sent)

                  elif task == 'trasnaltion':
                          trans= translation_pipeline(user_input)
                          return render_template("pipeline.html", trans=trans)


    

      
         
 







</body>
</html>





         
     

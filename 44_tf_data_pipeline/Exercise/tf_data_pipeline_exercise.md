Movie reviews are present as individual text file (one file per review) in review folder. 

Folder structure looks like this,
```
reviews
    |__ positive
        |__pos_1.txt
        |__pos_2.txt
        |__pos_3.txt
    |__ negative
        |__neg_1.txt
        |__neg_2.txt
        |__neg_3.txt
```   
You need to read these reviews using tf.data.Dataset and perform following transformations,

1. Read text review and generate a label from folder name. your dataset should have review text and label as a tuple
1. Filter blank text review. Two files are blank in this dataset
1. Do all of the above transformations in single line of code. Also shuffle all the reviews

[Solution](https://github.com/codebasics/deep-learning-keras-tf-tutorial/tree/master/44_tf_data_pipeline/Exercise/tf_data_pipeline_exercise_solution.ipynb)
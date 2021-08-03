To start docker container
==========================
```
docker run -it -v C:\Code\deep-learning-keras-tf-tutorial\48_tf_serving:/48_tf_serving -p 8601:8601 --entrypoint /bin/bash tensorflow/serving
```

To serve only latest model
===========================
```
tensorflow_model_server --rest_api_port=8601 --model_name=email_model --model_base_path=/saved_models/
```

To serve models using model config file
========================================
```
tensorflow_model_server --rest_api_port=8700  --allow_version_labels_for_unavailable_models --model_config_file=/48_tf_serving/model.config.c
```


Postman commands
=================

To call by versions
```
http://localhost:8502/v1/models/email_model/versions/2:predict
```

To call by labels
```
http://localhost:8502/v1/models/email_model/labels/stable:predict
```

Body: raw
```
{
    "instances": [
        "Let's meet for dinner tomorrow",
        "You are awarded a SiPix Digital Camera! call 09061221061 from landline. Delivery within 28days. T Cs Box177"
    ]
}
```

TF Serving Installation Instructions 
====================================

https://www.tensorflow.org/tfx/serving/docker
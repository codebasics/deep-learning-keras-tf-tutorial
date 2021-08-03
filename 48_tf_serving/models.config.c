model_config_list {
  config {
    name: 'email_model'
    base_path: '/48_tf_serving/saved_models'
    model_platform: 'tensorflow'
	model_version_policy {
	  specific {
		versions: 1
		versions: 2
	  }
	}
	version_labels {
	  key: 'production'
	  value: 1
	}
	version_labels {
	  key: 'beta'
	  value: 2
	}
  }
}


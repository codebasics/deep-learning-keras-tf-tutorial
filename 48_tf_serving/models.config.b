model_config_list {
  config {
    name: 'email_model'
    base_path: '/48_tf_serving/saved_models'
    model_platform: 'tensorflow'
    model_version_policy: {
		specific: {
			versions: 2
			versions: 3
		}
	}
  }
}


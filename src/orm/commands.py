

class Commands(object):
    def __init__(self, session):
        self.session = session

    def login(self, name, password):
        self.session.login(name, password)

    def logout(self, name):
        self.session.logout(name)

    def create_user(self, name, password):
        self.session.create_user(name, password)

    def extract_feature(self, fn, name, form):
        self.session.extract_feature(fn, name)

    def get_sample_dataset(self, form):
        return self.session.get_sample_dataset(form)

    def get_columns(self):
        return self.session.get_columns()

    def get_features(self, feature_name, user_name=None):
        return self.session.get_features(feature_name, user_name)

    def add_feature(self, feature_name):
        return self.session.add_feature(feature_name)

    def test(self, X, Y, test_size=0.5):
        return self.session.cross_validate(X, Y, test_size)

    def add_notebook(self, name):
        self.session.add_notebook(name)

    def cross_validate(self, X, Y, test_size):
        return self.session.cross_validate(X, Y, test_size)
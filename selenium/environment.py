
def before_all(context):
    print('before...')


def after_all(context):
    print('after all')


def before_feature(context, feature):
    pass
    # print(f'before feature {feature.name}...')


def after_feature(context, feature):
    pass
    # print(f'after feature {feature.name} {feature.status}...')


def before_scenario(context, scenario):
    pass
    # print(f'before scenario {scenario.tags}...')


def after_scenario(context, scenario):
    # print(f'after scenario {scenario.tags}...')
    pass

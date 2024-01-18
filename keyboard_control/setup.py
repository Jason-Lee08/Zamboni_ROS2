from setuptools import setup

package_name = 'keyboard_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'twist_keyboard'
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jason',
    maintainer_email='jason.lee@meditrina-inc.com',
    description='An improved robot-agnostic teleoperation node to convert keyboard'
                'commands to Twist messages.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard = twist_keyboard:main'
        ],
    },
)

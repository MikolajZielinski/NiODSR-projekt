from setuptools import setup

package_name = 'ur5_aruco_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mikolaj',
    maintainer_email='mikolaj.m.zielinski@student.put.poznan.pl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aruco_to_directions = ur5_aruco_control.aruco_to_directions:main',
            'directions_to_ur5_movement = ur5_aruco_control.directions_to_ur5_movement:main',
        ],
    },
)

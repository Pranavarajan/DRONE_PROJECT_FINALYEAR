from setuptools import setup

package_name = 'uav_core'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'uav_controller = uav_core.uav_controller:main',
            'battery_monitor = uav_core.battery_monitor:main'
        ],
    },
)

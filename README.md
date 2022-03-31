# Tune Static Transform

This package is meant to provide a convenient interface to tune a static transform, through the use of the dynamic reconfigure server.

## Usage

Simply start the server:
```
rosrun tune_static_transform server.py
```

And open a dynamic-reconfigure window through rqt:
```
rqt
```

## Limitations

- Because dynamic-reconfigure requires a min and max value for the numeric parameters, it could be that your required transform is out of bounds. This can be fixed by changing the min and max values in `cfg/TuneStaticTF.cfg`. By default the min/max are set to 3/-3.

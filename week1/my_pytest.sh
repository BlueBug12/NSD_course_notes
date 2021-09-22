g++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) exercise.cpp -o exercise$(python3-config --extension-suffix)
pytest test_exercise.py

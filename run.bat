rem pytest -s -v -m "sanity" --html=.\Reports\report.html  .\TestCases\
rem  pytest -s -v -m "sanity and regression" --html=.\Reports\report.html  .\TestCases\
rem pytest -s -v -m "sanity or regression" --html=.\Reports\report.html  .\TestCases\
pytest -s -v -m "regression" --html=.\Reports\report.html  .\TestCases\
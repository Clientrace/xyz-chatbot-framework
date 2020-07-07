
import sys

if __name__ == '__main__':
  sys.path.append('./')
  from core.e2e.validators import masterfile_validator

  print('Running validator..')
  for i in dir(masterfile_validator):
    item = getattr(masterfile_validator, i)
    if callable(item) and '_validate' in i:
      item()


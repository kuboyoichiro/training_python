
# -*- coding: utf-8 -*-

def helloWorld():
  print ('hello')

def executeArithmetic(leftArg, rightArg):
  add = leftArg + rightArg
  min = leftArg - rightArg
  mul = leftArg * rightArg
  div = leftArg / rightArg
  rem = leftArg % rightArg
  print (add, min, mul, div, rem)

def executeIf(leftArg, rightArg):
  if leftArg < rightArg:
    print ('right is big')
  elif rightArg < leftArg:
    print ('leftArg is big')
  else:
    print ('left and right are equal')

def executeFor(count):
  for i in range(count):
    print (i)

def fizzBuzz(count):
  fizz = list()
  buzz = list()
  fizzBuzz = list()
  for i in range(0, count + 1):
    if i % 3 == 0 and i % 5 == 0:
      fizzBuzz.append(i)
    elif i % 3 == 0:
      fizz.append(i)
    elif i % 5 == 0:
      buzz.append(i)

  print (fizz, buzz, fizzBuzz)

class Spam:
  __attr = 100
  def __init__(self,ham,egg):
    self.ham = ham
    self.egg = egg
  def output(self):
    sum = self.ham + self.egg
    print (self.__attr)
    print("{0}".format(sum))

def activateSpam():
  spam = Spam(5,10)
  spam.output()
  # print (spam.__attr) <- error!

class FizzBuzz:
  __limit = 0
  __fizz = list()
  __buzz = list()
  __fizzbuzz = list()

  def __init__(self, count):
    self.__limit = count
  
  def __rollUp(self):
    limit = self.__limit
    for i in range(1, limit + 1):
      if i % 3 == 0 and i % 5 == 0:
        self.__fizzbuzz.append(i)
      elif i % 3 == 0:
        self.__fizz.append(i)
      elif i % 5 == 0:
        self.__buzz.append(i)
    print (self.__fizz, self.__buzz, self.__fizzbuzz)

  def start(self):
    self.__rollUp()

def activateFizzBuzz(count):
  fizzBuzz = FizzBuzz(count)
  fizzBuzz.start()


class ExFizzBuzz(FizzBuzz):
  def exStart(self):
    print ('exStart')
    self.start()

def activateExFizzBuzz(count):
  exFizzBuzz = ExFizzBuzz(count)
  exFizzBuzz.exStart()

if __name__ == "__main__":
  activateExFizzBuzz(30)

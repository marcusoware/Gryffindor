import 'dart:io';

void main() {
  final cc = calcus();
  print(cc);
}




dynamic calcus() {
  print("enter number1 \n");
  dynamic num1 = stdin.readLineSync();
  num1 = int.parse(num1);

  // get num2 & convert to int
  print("enter number2 \n");
  dynamic num2 = stdin.readLineSync();
  num2 = int.parse(num2);

  // choose the operation

  print('\n ======== CALCULATOR MENU ========= \n');
  print(
    'choose your calculator method \n 1. [ADDITION] \n2. [SUBSTRACTION]\n3. [DIVISION] \n4. [MULTIPLICATON] \n',
  );
  dynamic operation = stdin.readLineSync();
  int op = int.parse(operation);

  if (op == 1) {
    return addition(num1: num1, num2: num2);
  } else if (op == 2) {
    return substraction(num1: num1, num2: num2);
  } else if (op == 3) {
    return division(num1: num1, num2: num2);
  } else if (op == 4) {
    return multiplication(num1: num1, num2: num2);
  } else {
    return "invalid user choice";
  }
}




//  CALCULATIONS


dynamic addition({required int num1, required int num2}) {
  var total = num1 + num2;
  return total;
}

dynamic substraction({required int num1, required int num2}) {
  var total = num1 + num2;
  return total;
}

dynamic division({required int num1, required int num2}) {
  if (num2 != 0) {
    var total = num1 / num2;
    return total;
  } else {
    return "can't divide by zero[0]";
  }
}

dynamic multiplication({required int num1, required int num2}) {
  var total = num1 * num2;
  return total;
}

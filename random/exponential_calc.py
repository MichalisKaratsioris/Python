import time

# Let's play with exponential calculation
#
# - Can you find the largest fibonacci number your computer can handle?
# - Count the number of operations that the fibonacci function performs, display it too

def fibonacci (number):
    if (number <= 1):
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)

nth_item = 10

start = time.process_time()

result = fibonacci( nth_item )

elapsed_time = time.process_time() - start

print( "The #{} fibonacci number is {} and it took {} sec to calculate".format( nth_item, result, elapsed_time ) )

"""
Java code
public class Exponential {

// Let's play with exponential calculation
//
// - Can you find the largest fibonacci number your computer can handle?
// - Count the number of operations that the fibonacci function performs, display it too


  public static void main(String[] args) {
    int nth_item = 1000;

    long start = System.nanoTime();

    int result = fibonacci(nth_item);

    double elapsedTime = (System.nanoTime() - start) / 1000000000.;

    System.out.println(String.format("The #%d fibonacci number is %d and it took %f sec to calculate", nth_item, result, elapsedTime));
  }

  private static int fibonacci(int number) {
    if (number <= 1) {
      return number;
    }
    return fibonacci(number - 2) + fibonacci(number - 1);
  }
}

"""
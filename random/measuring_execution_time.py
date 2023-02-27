import time

# This is a simple demonstration on how to measure execution time
# Try changing num_of_iterations to see how it affects running time

# Which O would it be?

c = 0
num_of_iterations = 500000
start = time.process_time()

for i in range( num_of_iterations ):
    c += 1

elapsed_time = time.process_time() - start

print(elapsed_time)

"""
Java code
public class MeasureTime {

// This is a simple demonstration on how to measure execution time
// Try changing num_of_iterations to see how it affects running time
//
// Which O would it be?

  public static void main(String[] args) {
    int c = 0;
    int numOfIterations = 500000;
    long start = System.nanoTime();

    for (int i = 0; i < numOfIterations; i++) {
      c += 1;
    }

    double elapsedTime = (System.nanoTime() - start) / 1000000000.;

    System.out.println(elapsedTime);
  }


}

"""
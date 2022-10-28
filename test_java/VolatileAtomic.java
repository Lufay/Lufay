public class VolatileAtomic {

  private static final int thread_num = 2;
  private static final int times = 1000;

  public static void main(String args[]) {
    MyTest myTest = new MyTest();
    for (int i = 1; i <= thread_num; i++) {
      new Thread(
        () -> {
          for (int j = 1; j <= times; j++) {
            myTest.addNum();
          }
        },
        String.valueOf(i)
      )
        .start();
    }
    // left until only self
    while (Thread.activeCount() > 1) {
      Thread.yield();
    }
    // not Equal to thread_num * times
    System.out.println(
      Thread.currentThread().getName() + "\t number= " + myTest.num
    );
  }
}

class MyTest {

  public volatile int num = 0;

  public void addNum() {
    num++;
  }
}

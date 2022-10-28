
import java.util.concurrent.*;


public class TestCountDownLatch {
 
    private static CountDownLatch countDownLatch = new CountDownLatch(1000);
    private volatile static int   num            = 0;
 
    public static void main(String[] args) {
        ExecutorService executor = Executors.newCachedThreadPool();
        for (int i = 0; i < 1000; i++) {
            executor.execute(() -> {
                try {
                    num++;
                } catch (Exception e) {
                    e.printStackTrace();
                } finally {
                    countDownLatch.countDown();
                }
            });
        }
        try {
            countDownLatch.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        executor.shutdown();
        System.out.println(num);
    }
}
public class Singleton {
 
    private volatile static Singleton instance;     // 禁止指令重排
 
    private Singleton() {}
 
    public static Singleton getInstance() {
        if (instance == null) {                     // 减轻加锁负担
            synchronized (Singleton.class) {
                if (instance == null) {             // double check，因为在锁住之前可能有多个线程通过了第一次检查
                    instance = new Singleton();     // 非原子的3个动作：1. 分配内存；2. 初始化；3. 使instance 指向该内存空间（2、3步没有依赖关系，可以重排序）。所以有可能instance 还没初始化完成，就被另一个线程返回了
                }
            }
        }
        return instance;
    }
}
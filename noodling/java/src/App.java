import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class App {
    public static void main(String[] args) throws Exception {

        final int size = 5;
        String[] strings = new String[size];
        ExecutorService executor = Executors.newFixedThreadPool(size);
        Future<String>[] futures = new Future[size];
        for (int i = 0; i < size; ++i)
            strings[i] = "String " + (i + 1) + ", ";
        for (int i = 0; i < size; ++i) {
            final int index = i;
            futures[i] = executor.submit(() -> strings[index]);
        }
        StringBuilder result = new StringBuilder();
        for (Future<String> future : futures) {
            try {
                result.append(future.get());
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }
        }
        System.out.println("Concatenated String: " + result.toString());
        executor.shutdown();
    }
}

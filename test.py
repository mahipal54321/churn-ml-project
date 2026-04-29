import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ChurnClient {
    public static void main(String[] args) {
        try {
            HttpClient client = HttpClient.newHttpClient();

            String json = """
            {
              "tenure": 1,
              "MonthlyCharges": 95.0,
              "TotalCharges": 95.0,
              "SeniorCitizen": 1,
              "Partner": "No",
              "Dependents": "No",
              "PhoneService": "Yes",
              "InternetService": "Fiber optic",
              "Contract": "Month-to-month"
            }
            """;

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("http://127.0.0.1:8000/predict"))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(json))
                    .build();

            HttpResponse<String> response =
                    client.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("Response:");
            System.out.println(response.body());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
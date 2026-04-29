package com.example.demo;

import org.springframework.web.bind.annotation.*;
import java.net.URI;
import java.net.http.*;

@RestController
@RequestMapping("/churn")
public class ChurnController {

    @PostMapping("/predict")
    public String predict(@RequestBody String json) {
        try {
            HttpClient client = HttpClient.newHttpClient();

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("http://127.0.0.1:8000/predict"))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(json))
                    .build();

            HttpResponse<String> response =
                    client.send(request, HttpResponse.BodyHandlers.ofString());

            return response.body();

        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
    }
}
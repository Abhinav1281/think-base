package thinkbase.service;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.client.RestTemplate;

@Service
public class CoreInteractionService {
    
    private final RestTemplate restTemplate;

    @Value("${core.service.base-url}")
    private String coreUrl;

    public CoreInteractionService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public String getCoreStatus() {
        String url = coreUrl + "/health";
        return restTemplate.getForObject(url, String.class);
    }
}

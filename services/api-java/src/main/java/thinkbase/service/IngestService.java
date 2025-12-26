package thinkbase.service;

import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.ObjectMapper;

import thinkbase.model.IngestionModel;

@Service
public class IngestService {
    private static String rabbitmq_queue = System.getenv("RABBITMQ_QUEUE");
    public boolean ingestData(IngestionModel data) throws Exception {
        ObjectMapper objectMapper = new ObjectMapper();
        String jsonData = objectMapper.writeValueAsString(data);
        RabbitMQService.sendMessage(jsonData, rabbitmq_queue);
        return true;
    }
}

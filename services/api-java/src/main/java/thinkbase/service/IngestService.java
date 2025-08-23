package thinkbase.service;

import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.ObjectMapper;

import thinkbase.model.IngestionModel;

@Service
public class IngestService {
    public boolean ingestData(IngestionModel data) throws Exception {
        ObjectMapper objectMapper = new ObjectMapper();
        String jsonData = objectMapper.writeValueAsString(data);
        RabbitMQService.sendMessage(jsonData, "ingest_queue");
        return true;
    }
}

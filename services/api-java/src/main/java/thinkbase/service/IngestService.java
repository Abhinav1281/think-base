package thinkbase.service;

import org.springframework.stereotype.Service;

@Service
public class IngestService {
    public boolean ingestData(String data) throws Exception {
        RabbitMQService.sendMessage(data, "ingest_queue");
        return true;
    }
}

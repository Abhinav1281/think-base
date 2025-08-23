package thinkbase.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import thinkbase.model.IngestionModel;
import thinkbase.service.*;

@RestController
@RequestMapping("/api")
public class basicController {

    @Autowired
    private IngestService ingestService;
    @Autowired
    private CoreInteractionService coreInteractionService;

    @GetMapping("/health")
    public ResponseEntity<String> healthCheck() {
        return new ResponseEntity<>("THINKBASE API : OK", HttpStatus.OK);
    }

    @GetMapping("/core-health")
    public ResponseEntity<String> coreHealthCheck() {
        return new ResponseEntity<>(coreInteractionService.getCoreStatus(), HttpStatus.OK);
    }

    @PostMapping("/ingest")
    public ResponseEntity<Boolean> ingest(@RequestBody IngestionModel ingestionBody) {
        try {
            return new ResponseEntity<>(ingestService.ingestData(ingestionBody), HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>(false, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}

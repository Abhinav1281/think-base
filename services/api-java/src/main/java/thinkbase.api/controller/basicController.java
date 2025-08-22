package thinkbase.api.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import thinkbase.api.service.IngestService;

@RestController
@RequestMapping("/api")
public class basicController {

    @Autowired
    private IngestService ingestService;

    @GetMapping("/health")
    public String hello() {
        return "ThinkBase API is UP!";
    }

    @PostMapping("/ingest")
    public ResponseEntity<Boolean> ingest(@RequestBody String name) {
        try {
            return new ResponseEntity<>(ingestService.ingestData(name), HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>(false, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}

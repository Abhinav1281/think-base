package thinkbase.model;

import lombok.Data;

@Data
public class IngestionModel {
    private String doc_id;
    private String content;
    private String source;
    private Object[] metadata;
}

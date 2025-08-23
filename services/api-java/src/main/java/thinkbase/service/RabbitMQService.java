package thinkbase.service;

import com.rabbitmq.client.*;

public class RabbitMQService {
    private static String host = System.getenv("RABBITMQ_HOST");

    public static void sendMessage(String message, String queueName) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(host);
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();
        channel.queueDeclare(queueName, true, false, false, null);
        channel.basicPublish("", queueName, null, message.getBytes("UTF-8"));
        channel.close();
        connection.close();
    }
}

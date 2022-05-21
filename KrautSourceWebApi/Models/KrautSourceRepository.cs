using MQTTnet;
using MQTTnet.Client;
using MQTTnet.Client.Options;
using System;
using System.Text.Json;
using System.Threading.Tasks;

namespace KrautSourceWebApi.Models
{
    public class KrautSourceRepository : IKrautSourceRepository
    {
        private readonly KrautDbContext context;

        public KrautSourceRepository(KrautDbContext _context)
        {
            context = _context;
        }

        public async void CreateData(Data data)
        {
            data.Position.idLocation = Guid.NewGuid().ToString();
            data.InsertTime = DateTime.Now;
            context.Data.Add(data);
            context.SaveChanges();


            MqttFactory mqttFactory = new MqttFactory();
            IMqttClient client = mqttFactory.CreateMqttClient();
            var options = new MqttClientOptionsBuilder()
                .WithClientId(Guid.NewGuid().ToString())
                .WithTcpServer("mqtt.datapool.opendatahub.testingmachine.eu", 1883)
                .WithCleanSession().Build();

            await client.ConnectAsync(options);

            await PublishMessageAsync(client, data);

            await client.DisconnectAsync();
        }

        private static async Task PublishMessageAsync(IMqttClient client, Data data)
        {
            string json = JsonSerializer.Serialize(data);
            var message = new MqttApplicationMessageBuilder()
                .WithTopic("/open/hackathon-2022/crowdsourced-data-sharing")
                .WithPayload(json)
                .WithAtLeastOnceQoS().Build();

            if (client.IsConnected)
            {
                await client.PublishAsync(message);
            }
        }
    }
}

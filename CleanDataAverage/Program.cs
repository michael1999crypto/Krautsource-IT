using MySql.Data.MySqlClient;
using System;
using System.Data;

namespace CleanDataAverage
{
    //Example of cleaner data microservice

    internal class Program
    {
        public static string tmpConnectionString = "server=localhost;user id = root; database=krautSourceDB; password=laspo";

        static void Main(string[] args)
        {
            DataTable dtData = new DataTable();
            using(MySqlConnection conn = new MySqlConnection(tmpConnectionString))
            {
                MySqlCommand cmd = new MySqlCommand("select * from data d join location l on (d.PositionIdLocation = l.idLocation)" +
                    "where d.InsertTime > (now() - interval 10 minute)", conn);
                MySqlDataAdapter da = new MySqlDataAdapter(cmd);
                da.Fill(dtData);
            }

            double meters = 10; //value random only for trying
            foreach (DataRow row in dtData.Rows)
            {
                DataRow[] ridondantDatas = dtData.Select($"longitude < {Convert.ToDouble(row["longitude"]) + meters} " +
                    $"AND longitude > {Convert.ToDouble(row["longitude"]) - meters} " +
                    $"AND latitude < {Convert.ToDouble(row["latitude"]) + meters} " +
                    $"AND latitude > {Convert.ToDouble(row["latitude"]) - meters}");

                double sum = 0;
                for (int i = 0; i < ridondantDatas.Length; i++)
                {
                    sum += Convert.ToDouble(ridondantDatas[i]["value"].ToString());
                }

                double average = sum / ridondantDatas.Length;

                SendToBrokerMQTT(row, average);

                RemoveRedondantDataFromDt(ridondantDatas, dtData);

            }
        }

        private static void SendToBrokerMQTT(DataRow row, double average)
        {
            throw new NotImplementedException();
        }

        private static void RemoveRedondantDataFromDt(DataRow[] ridondantDatas, DataTable dtData)
        {
            throw new NotImplementedException();
        }
    }
}

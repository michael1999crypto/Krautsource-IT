using System;

namespace KrautSourceWebApi.Models
{
    public class Data
    {
        public string TypeOfData { get; set; }
        public string Location { get; set; }
        public Location Position { get; set; }
        public DateTimeOffset InsertTime { get; set; }
    }
}

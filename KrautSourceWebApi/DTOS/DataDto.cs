using KrautSourceWebApi.Models;
using System;

namespace KrautSourceWebApi.DTOS
{
    public class DataDto
    {
        public string TypeOfData { get; set; }

        public string Value { get; set; }

        public Location Position { get; set; }

        public DateTimeOffset InsertTime { get; set; }
    }
}

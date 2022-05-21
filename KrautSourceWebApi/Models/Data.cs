using System;
using System.ComponentModel.DataAnnotations;

namespace KrautSourceWebApi.Models
{
    public class Data
    {
        [Required]
        public string Id { get; set; }

        public string ConsumerType { get; set; }

        [Required]
        public string TypeOfData { get; set; }

        [Required]
        public string Value { get; set; }

        public Location Position { get; set; }

        public DateTimeOffset InsertTime { get; set; }
    }
}

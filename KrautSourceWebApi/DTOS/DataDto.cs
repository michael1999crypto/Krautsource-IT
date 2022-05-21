﻿using KrautSourceWebApi.Models;
using System;

namespace KrautSourceWebApi.DTOS
{
    public class DataDto
    {
        public string Id { get; set; }

        public string ConsumerType { get; set; }

        public string TypeOfData { get; set; }

        public string Value { get; set; }

        public LocationDto Position { get; set; }

        public DateTimeOffset InsertTime { get; set; }
    }
}

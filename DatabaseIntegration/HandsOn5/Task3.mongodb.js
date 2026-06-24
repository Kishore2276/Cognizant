use("college_nosql");


db.feedback.aggregate([
    { $match: { semester: "2022-ODD" } },
    {
        $group: {
            _id: "$course_code",
            avg_rating: { $avg: "$rating" },
            total_feedback: { $sum: 1 }
        }
    },
    { $sort: { avg_rating: -1 } }
]);


db.feedback.aggregate([
    { $match: { semester: "2022-ODD" } },
    {
        $group: {
            _id: "$course_code",
            avg_rating: { $avg: "$rating" },
            total_feedback: { $sum: 1 }
        }
    },
    {
        $project: {
            _id: 0,
            course_code: "$_id",
            average_rating: { $round: ["$avg_rating", 1] },
            total_feedback: 1
        }
    },
    { $sort: { average_rating: -1 } }
]);


db.feedback.aggregate([
    { $unwind: "$tags" },
    {
        $group: {
            _id: "$tags",
            tag_count: { $sum: 1 }
        }
    },
    { $sort: { tag_count: -1 } }
]);


db.feedback.createIndex({ course_code: 1 });

db.feedback.find({
    course_code: "CS101"
}).explain("executionStats");
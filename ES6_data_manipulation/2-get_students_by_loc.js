function getStudentsByLocation() {
    if(!Array.isArray(students)) {
        return [];
    }

    const result = students.filer((item) => item.location === city);

    return result;
}

export default getStudentsByLocation;

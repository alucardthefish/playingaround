import { Component, OnInit } from '@angular/core';
import { JobsService } from "../jobs.service"

@Component({
  selector: 'app-jobs',
  templateUrl: './jobs.component.html',
  styleUrls: ['./jobs.component.css']
})
export class JobsComponent implements OnInit {

  componentName: string = "Jobs"
  jobs: any;

  constructor(private jobsService: JobsService) { }

  ngOnInit() {
  	this.jobsService.getAllJobs().subscribe(
  		res => { 
  			this.jobs = res["data"];
  			console.log("jobs: ", this.jobs); 
  		},
  		error => console.log("error: ", error)
  	);
  }

}
